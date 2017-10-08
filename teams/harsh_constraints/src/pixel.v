`timescale 1ns / 1ps

module pixel(
    // all inputs are binary, not differential!
    clk_fast,
    clk_slow,
    rx0,
    rx1,
    rx2,
    rx3,
    rst_n,
    locked,
    // output
    data,
    valid,
    clkout
    );
    
    input wire locked;
    wire locked_q;
    assign locked_q = ~locked;
    input clk_fast;
    input clk_slow;
    input rx0;
    input rx1;
    input rx2;
    input rx3;
    input rst_n;
    output reg [7:0] data;
    output wire clkout;
    output reg valid;
    reg [7:0] int_data;
    reg [6:0] rx0_reg;
    reg [6:0] rx1_reg;
    reg [6:0] rx2_reg;
    reg [6:0] rx3_reg;
    reg dval;
    reg fval;
    reg lval;

    wire rst;
    assign rst = ~rst_n;
    assign clkout = clk_fast;
    parameter SIZE = 3;
    reg [SIZE-1:0] state;
    reg [SIZE-1:0] next_state;
    
    parameter IDLE = 3'b001, // not locked
        WAITING = 3'b010,   // for frame sync lock
        STREAMING = 3'b100; // includes line sync

    always @(state or locked or fval)
    begin: FSM_switch
        next_state = 3'b000;
        case(state)
            IDLE: if ( locked == 1 ) begin
                    next_state = WAITING;
                    end else begin
                        next_state = IDLE;
                    end
            WAITING: if ( dval == 1) begin
                        next_state = STREAMING;
                    end else if ( fval == 1) begin
                        next_state = STREAMING;
                    end else if ( locked == 0) begin
                        next_state = IDLE;
                    end else begin
                        next_state = WAITING;
                    end
            STREAMING: if (fval == 0) begin
                        next_state = WAITING;
                    end else if (locked == 0) begin
                        next_state = IDLE;
                    end else begin
                        next_state = STREAMING;
                    end
            default: next_state = IDLE;
         endcase
    end
  // sequential logic
    always @(posedge clk_fast) 
    begin : FSM_sequence
        if (rst) begin
            state <= IDLE;
        end else begin
            state <= next_state;
        end
    end
    
    reg [3:0] counter;
    
    always @(posedge clk_fast)
    begin: FSM_out
    case (state)
        IDLE: valid <= 1'b0;
        WAITING: begin
                    valid <= 1'b0;  
                    if (counter <= 6) begin
                        rx0_reg <= {rx0_reg[5:0],rx0};
                        rx1_reg <= {rx1_reg[5:0],rx1};
                        rx2_reg <= {rx2_reg[5:0],rx2};
                        rx3_reg <= {rx3_reg[5:0],rx3};
                        counter <= counter + 1;
                    end
                    if (counter > 6) begin
                        counter <= 0;
                        int_data [2] = rx0_reg[0];
                        int_data [3] = rx1_reg[6];
                        int_data [4] = rx1_reg[5];
                        int_data [5] = rx1_reg[4];
                        int_data [6] = rx1_reg[3];
                        int_data [7] = rx1_reg[2];
                        int_data [1] = rx3_reg[5];  
                        int_data [0] = rx3_reg[6];
                        dval = rx2_reg[0];
                        fval = rx2_reg[1];
                        lval = rx2_reg[2];
                    end
                 end
        STREAMING: begin
                    if (counter <= 6) begin
                        rx0_reg <= {rx0_reg[5:0],rx0};
                        rx1_reg <= {rx1_reg[5:0],rx1};
                        rx2_reg <= {rx2_reg[5:0],rx2};
                        rx3_reg <= {rx3_reg[5:0],rx3};
                        counter <= counter + 1;
                    end
                    if (counter > 6) begin
                        counter <= 0;
                        int_data [2] = rx0_reg[0];
                        int_data [3] = rx1_reg[6];
                        int_data [4] = rx1_reg[5];
                        int_data [5] = rx1_reg[4];
                        int_data [6] = rx1_reg[3];
                        int_data [7] = rx1_reg[2];
                        int_data [1] = rx3_reg[5];  
                        int_data [0] = rx3_reg[6];
                        dval = rx2_reg[0];
                        fval = rx2_reg[1];
                        lval = rx2_reg[2];
                        data = int_data;
                        valid <= 1'b1;
                    end
                  end
    endcase
    end
    
       
    
    // FVAL 0 means between frames
    // LVAL 0 means between lines
    // DVAL 1 means data is valid

    // state can be 2'd0, 2'd1, 2'd2, or 2'd3
    // 0 means uninitialized
    // 1 means it's a good pixel
    // 2 means it's inbetween lines
    // 3 means it's inbetween frames


    
endmodule
