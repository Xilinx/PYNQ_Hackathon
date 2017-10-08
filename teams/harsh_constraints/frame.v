module frame (
    // inputs
    clk,
    data,
    state,
   
    
    // outputs
    rst,
    frame_data,     
    valid
    );
    
    input clk;
    input [7:0] data;
    input [1:0] state;
    
    reg [7:0] pixel;
    
    reg [8:0] c;
    reg [7:0] r;
    
    reg [2559:0] row;
    
    reg [614399:0] frame;
    
    output reg [614399:0] frame_data; // can this synthesize?
    output reg valid = 0; // initial frame is invalid
     
    always @(posedge clk)
        begin
            if (state == 1)
                begin
                    pixel <= data;
                    if (c <= 319)
                        begin
                            row <= {row[2551:0],pixel};
                            c <= c + 1; // jump to next column (next pixel in row)
                        end
                    else
                        begin
                            if (r <= 239)
                                begin
                                    frame <= {frame[611839:0],row};
                                    c = 0; // reset column to zero
                                    r <= r + 1; // jump to next row
                                    valid = 0; // data is now invalid if frame has been modified
                                end
                            else
                                begin
                                    valid = 1; // data is valid until next row is filled (>= 320 clocks)
                                end
                        end
                end
        end
        
endmodule