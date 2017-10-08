//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/07/2017 09:39:31 AM
// Design Name: 
// Module Name: cameraclock
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

`timescale 1ns / 1ps

module cameraclock(
    input clk_in1_p,
    input clk_in1_n,
    output clk_fast,
    output clk_slow, 
    output locked
    );
    
    wire clk_in1_system_clk_wiz_0_0;
    assign clk_slow = clk_in1_system_clk_wiz_0_0;

    IBUFDS clkin1_ibufgds
       (.O  (clk_in1_system_clk_wiz_0_0),
        .I  (clk_in1_p),
        .IB (clk_in1_n));
    
    
      // Clocking PRIMITIVE
      //------------------------------------
    
      // Instantiation of the MMCM PRIMITIVE
      //    * Unused inputs are tied off
      //    * Unused outputs are labeled unused
    
      wire        clk_out1_system_clk_wiz_0_0;
      wire        clk_out2_system_clk_wiz_0_0;
      wire        clk_out3_system_clk_wiz_0_0;
      wire        clk_out4_system_clk_wiz_0_0;
      wire        clk_out5_system_clk_wiz_0_0;
      wire        clk_out6_system_clk_wiz_0_0;
      wire        clk_out7_system_clk_wiz_0_0;
    
      wire [15:0] do_unused;
      wire        drdy_unused;
      wire        psdone_unused;
      wire        locked_int;
      wire        clkfbout_system_clk_wiz_0_0;
      wire        clkfbout_buf_system_clk_wiz_0_0;
      wire        clkfboutb_unused;
      wire clkout0b_unused;
      wire clkout1b_unused;
      wire clkout2_unused;
      wire clkout2b_unused;
      wire clkout3_unused;
      wire clkout3b_unused;
      wire clkout4_unused;
      wire        clkout5_unused;
      wire        clkout6_unused;
      wire        clkfbstopped_unused;
      wire        clkinstopped_unused;
      wire        reset_high;
    
      MMCME2_ADV
      #(.BANDWIDTH            ("OPTIMIZED"),
        .CLKOUT4_CASCADE      ("FALSE"),
        .COMPENSATION         ("ZHOLD"),
        .STARTUP_WAIT         ("FALSE"),
        .DIVCLK_DIVIDE        (1),
        .CLKFBOUT_MULT_F      (49.000),
        .CLKFBOUT_PHASE       (102.857),
        .CLKFBOUT_USE_FINE_PS ("FALSE"),
        .CLKOUT0_DIVIDE_F     (7.000),
        .CLKOUT0_PHASE        (0.000),
        .CLKOUT0_DUTY_CYCLE   (0.500),
        .CLKOUT0_USE_FINE_PS  ("FALSE"),
        .CLKOUT1_DIVIDE       (49),
        .CLKOUT1_PHASE        (0.000),
        .CLKOUT1_DUTY_CYCLE   (0.7142),
        .CLKOUT1_USE_FINE_PS  ("FALSE"),
        .CLKIN1_PERIOD        (48.611))
      mmcm_adv_inst
        // Output clocks
       (
        .CLKFBOUT            (clkfbout_system_clk_wiz_0_0),
        .CLKFBOUTB           (clkfboutb_unused),
        .CLKOUT0             (clk_out1_system_clk_wiz_0_0),
        .CLKOUT0B            (clkout0b_unused),
        .CLKOUT1             (clk_out2_system_clk_wiz_0_0),
        .CLKOUT1B            (clkout1b_unused),
        .CLKOUT2             (clkout2_unused),
        .CLKOUT2B            (clkout2b_unused),
        .CLKOUT3             (clkout3_unused),
        .CLKOUT3B            (clkout3b_unused),
        .CLKOUT4             (clkout4_unused),
        .CLKOUT5             (clkout5_unused),
        .CLKOUT6             (clkout6_unused),
         // Input clock control
        .CLKFBIN             (clkfbout_system_clk_wiz_0_0),
        .CLKIN1              (clk_in1_system_clk_wiz_0_0),
        .CLKIN2              (1'b0),
         // Tied to always select the primary input clock
        .CLKINSEL            (1'b1),
        // Ports for dynamic reconfiguration
        .DADDR               (7'h0),
        .DCLK                (1'b0),
        .DEN                 (1'b0),
        .DI                  (16'h0),
        .DO                  (do_unused),
        .DRDY                (drdy_unused),
        .DWE                 (1'b0),
        // Ports for dynamic phase shift
        .PSCLK               (1'b0),
        .PSEN                (1'b0),
        .PSINCDEC            (1'b0),
        .PSDONE              (psdone_unused),
        // Other control and status signals
        .LOCKED              (locked_int),
        .CLKINSTOPPED        (clkinstopped_unused),
        .CLKFBSTOPPED        (clkfbstopped_unused),
        .PWRDWN              (1'b0),
        .RST                 (reset_high));
    
        assign locked = locked_int;

   
    // Clock Monitor clock assigning
    //--------------------------------------
     // Output buffering
      //-----------------------------------
    
//      BUFG clkf_buf
//       (.O (clkfbout_buf_system_clk_wiz_0_0),
//        .I (clkfbout_system_clk_wiz_0_0));
    
    
    
      BUFG clkout1_buf
       (.O   (clk_fast),
        .I   (~clk_out1_system_clk_wiz_0_0));
    
    
//      BUFG clkout2_buf
//       (.O   (clk_out2),
//        .I   (~clk_out2_system_clk_wiz_0_0));

    
    
endmodule
