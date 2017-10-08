`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/07/2017 02:25:40 PM
// Design Name: 
// Module Name: pixel_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module pixel_tb(
    
    );
    logic clk_fast, clk_slow, rx0, rx1, rx2, rx3, rst_n, valid, clkout, locked;
    logic [7:0] data;
    
    logic clk_in1_p, clk_in1_n;
    
    cameraclock cameraclock_inst(
//        input clk_in1_p,
//        input clk_in1_n,
//        output clk_out1,
//        output clk_out2
          .*
        );
        
    
    assign clk_in1_n = ~clk_in1_p;
    
    
    
    initial begin 

        clk_in1_p = 1;
        
        rst_n = 0;
        
        rst_n <= #100 1;
        
        forever begin
            clk_in1_p = #14 0;
            clk_in1_p = #21 1;
            #14;
        end
    
    end
    
    integer rx0temp;
    integer rx1temp;
    integer rx2temp;
    integer rx3temp;
    integer i;
    integer counter;
    initial begin
        while (~rst_n)        
            @(posedge clk_fast);
        
        i = 0;
        rx0temp = 14'b10000001000000;
        rx1temp = 14'b00111110011111;
        rx2temp = 14'b01000001000000;
        rx3temp = 14'b00000110000011;
        counter = 64'd10000000;
        while (counter < 1000000000) begin
            rx0 <= rx0temp[i];
            rx1 <= rx1temp[i]; 
            rx2 <= rx2temp[i];
            rx3 <= rx3temp[i];
            i = i + 1;
            counter += 1;
            @(posedge clk_fast);
            if (i > 13) begin
                i = 0;
            end
        end
    
    end
    
    
    
    
    pixel pixel_inst(
        // all inputs are binary, not differential!
//        clk_fast,
//        clk_slow,
//        rx0,
//        rx1,
//        rx2,
//        rx3,
//        rst,
//        // output
//        data,
//        valid,
//        clkout
          .*
        );    
    
    
    
endmodule
