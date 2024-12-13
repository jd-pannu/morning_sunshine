 
#include <cmath>
#include <stdint.h>
#include "tm4c1294ncpdt.h"
#include "vl53l1x_api.h"
#include "PLL.h"
#include "SysTick.h"
#include "uart.h"
#include "onboardLEDs.h"


void PortE0E1_Init(void){	
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R4;		              // activate the clock for Port E
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R4) == 0){};	        // allow time for clock to stabilize
  
	GPIO_PORTE_DIR_R = 0b00000011;
	GPIO_PORTE_DEN_R = 0b00000011;                        		// Enabled both as digital outputs
	return;
	}


void PortM0M1_Init(void){
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R11;                 //activate the clock for Port M
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R11) == 0){};        //allow time for clock to stabilize 
	GPIO_PORTM_DIR_R = 0b00000000;       								    // make PM0 an input, PM0 is reading if the button is pressed or not 
  GPIO_PORTM_DEN_R = 0b00000011;
	return;
}


//Enable D2, D1
void PortN0N1_Init(void){
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R12;                 //activate the clock for Port N
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R12) == 0){};
	GPIO_PORTN_DIR_R=0b00000011;
	GPIO_PORTN_DEN_R=0b00000011;
	return;
}

//Enable D3, D4
void PortF0F4_Init(void){
  SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R5;                 //activate the clock for Port F
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R5) == 0){};
	GPIO_PORTF_DIR_R=0b00010001;
	GPIO_PORTF_DEN_R=0b00010001;
	return;
}
void PortH_Init(void){
	//Use PortM pins for output
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R7;				// activate clock for Port H
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R7) == 0){};	// allow time for clock to stabilize
	GPIO_PORTH_DIR_R |= 0xFF;        								// make PH0 output
  GPIO_PORTH_AFSEL_R &= ~0xFF;     								// disable alt funct on PH
  GPIO_PORTH_DEN_R |= 0xFF;        								// enable digital I/O on PH
																									// configure PH as GPIO
  //GPIO_PORTM_PCTL_R = (GPIO_PORTM_PCTL_R&0xFFFFFF0F)+0x00000000;
  GPIO_PORTH_AMSEL_R &= ~0xFF;     								// disable analog functionality on PH		
	return;
}

void spin_cw(){
	for(int i=0; i<64; i++){ //this for loop is only meant to run the stepper moter for 45 degrees since full rotation is 512 and by dividing by 8 its 64 which is 360/8 45. 
		GPIO_PORTH_DATA_R = 0b00001001;
		SysTick_Wait10ms(1);
		GPIO_PORTH_DATA_R = 0b00000011;
		SysTick_Wait10ms(1);
		GPIO_PORTH_DATA_R = 0b00000110;
		SysTick_Wait10ms(1);
		GPIO_PORTH_DATA_R = 0b00001100;
		SysTick_Wait10ms(1);
	}
	GPIO_PORTN_DATA_R^=0b00000010;
	SysTick_Wait10ms(1);
	GPIO_PORTN_DATA_R^=0b00000010;
}

void spin_ccw(){
	for(int i=0; i<64; i++){ //this for loop is only meant to run the stepper moter for 45 degrees since full rotation is 512 and by dividing by 8 its 64 which is 360/8 45. 
		GPIO_PORTH_DATA_R = 0b00001100;
		SysTick_Wait10ms(1);
		GPIO_PORTH_DATA_R = 0b00000110;
		SysTick_Wait10ms(1);
		GPIO_PORTH_DATA_R = 0b00000011;
		SysTick_Wait10ms(1);
		GPIO_PORTH_DATA_R = 0b00001001;
		SysTick_Wait10ms(1);
	}
	GPIO_PORTN_DATA_R^=0b00000010;
	SysTick_Wait10ms(1);
	GPIO_PORTN_DATA_R^=0b00000010;
}


int main(void){
	PLL_Init();
	SysTick_Init();
	PortE0E1_Init();
	PortM0M1_Init();
	PortN0N1_Init();
	PortF0F4_Init();
	PortH_Init();
	UART_Init();
	
	//turn off LEDs at reset
	GPIO_PORTF_DATA_R = 0b00000000;
	
	int input = 0;
	int range = 1;
	
	while(1){
		input = UART_InChar();//waiting for enter from python to open the port 4 for UART connection 
		if (input == 's'){
			while(1){//keep checking if the button is pressed 
		

				for (int i = 0; i<8; i++){
					
					spin_cw();
				}

				SysTick_Wait10ms(3);
				
				for (int i = 0; i<8; i++){
					
					spin_ccw();
				
				}
				SysTick_Wait10ms(500);
				
				if(GPIO_PORTM_DATA_R == 0b00000000){ //since it is an active low it is constantly 1 and when the button is pressed it turns 0
					break;
				}


		}
		break;
		}

		
	}
		
	
	UART_printf("Program Begins\r\n");
	int mynumber = 1;
	sprintf(printf_buffer,"2DX4 Program Studio Code %d\r\n",mynumber);
	UART_printf(printf_buffer);
		
	

	

		
		
		
		//Drive Low (assign 0) PE0 (Row 0) for scanning
		
		
		//Write a code that while # is pressed, D3 is turned ON
		//(hint: Use the while loop for checking)
		

		//Write a code that while D is pressed, D4 is turned ON
		//(hint: Use the while loop for checking)
		
		
	}


