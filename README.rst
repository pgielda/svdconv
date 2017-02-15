simple SVD XML parser example

usage
=====

execute: ``./svdparse.py example_svds/STM32F41x.svd.gz`` 
to get this result:

::
	>>> Parsing SVD file 'example_svds/STM32F41x.svd.gz'...
	--- XML parsed.
	--- SVD parsed.
	<<< File parsed.
	peripheral: 'ADC1' of type 'ADC', registered @ <40012000..40012400), with interrupts: 'ADC_IRQ' @ 18 
	peripheral: 'ADC2' of type 'ADC', registered @ <40012100..40012500), with interrupts: 'ADC_IRQ' @ 18 
	peripheral: 'ADC3' of type 'ADC', registered @ <40012200..40012600), with interrupts: 'ADC_IRQ' @ 18 
	peripheral: 'CAN1' of type 'CAN', registered @ <40006400..40006800), with interrupts: 'CAN1_TX_IRQ' @ 19 , 'CAN1_RX0_IRQ' @ 20 , 'CAN1_RX1_IRQ' @ 21 , 'CAN1_SCE_IRQ' @ 22 
	peripheral: 'CAN2' of type 'CAN', registered @ <40006800..40006C00), with interrupts: 'CAN2_TX_IRQ' @ 63 , 'CAN2_RX0_IRQ' @ 64 , 'CAN2_RX1_IRQ' @ 65 , 'CAN2_SCE_IRQ' @ 66 
	peripheral: 'CRC' of type 'CRC', registered @ <40023000..40023400)
	peripheral: 'CRYP' of type 'CRYP', registered @ <50060000..50060400), with interrupts: 'CRYP_IRQ' @ 79 
	peripheral: 'C_ADC' of type 'ADC', registered @ <40012300..40012700)
	peripheral: 'DAC' of type 'DAC', registered @ <40007400..40007800), with interrupts: 'TIM6_DAC_IRQ' @ 54 
	peripheral: 'DBG' of type 'DBG', registered @ <E0042000..E0042400)
	peripheral: 'DCMI' of type 'DCMI', registered @ <50050000..50050400), with interrupts: 'DCMI_IRQ' @ 78 
	peripheral: 'DMA1' of type 'DMA', registered @ <40026000..40026400), with interrupts: 'DMA1_Stream0_IRQ' @ 11 , 'DMA1_Stream1_IRQ' @ 12 , 'DMA1_Stream2_IRQ' @ 13 , 'DMA1_Stream3_IRQ' @ 14 , 'DMA1_Stream4_IRQ' @ 15 , 'DMA1_Stream5_IRQ' @ 16 , 'DMA1_Stream6_IRQ' @ 17 , 'DMA1_Stream7_IRQ' @ 47 
	peripheral: 'DMA2' of type 'DMA', registered @ <40026400..40026800), with interrupts: 'DMA2_Stream0_IRQ' @ 56 , 'DMA2_Stream1_IRQ' @ 57 , 'DMA2_Stream2_IRQ' @ 58 , 'DMA2_Stream3_IRQ' @ 59 , 'DMA2_Stream4_IRQ' @ 60 , 'DMA2_Stream5_IRQ' @ 68 , 'DMA2_Stream6_IRQ' @ 69 , 'DMA2_Stream7_IRQ' @ 70 
	peripheral: 'EXTI' of type 'EXTI', registered @ <40013C00..40014000), with interrupts: 'TAMP_STAMP_IRQ' @ 2 , 'EXTI0_IRQ' @ 6 , 'EXTI1_IRQ' @ 7 , 'EXTI2_IRQ' @ 8 , 'EXTI3_IRQ' @ 9 , 'EXTI4_IRQ' @ 10 , 'EXTI9_5_IRQ' @ 23 , 'EXTI15_10_IRQ' @ 40 
	peripheral: 'Ethernet_DMA' of type 'Ethernet', registered @ <40029000..40029400)
	peripheral: 'Ethernet_MAC' of type 'Ethernet', registered @ <40028000..40028400), with interrupts: 'ETH_IRQ' @ 61 , 'ETH_WKUP_IRQ' @ 62 
	peripheral: 'Ethernet_MMC' of type 'Ethernet', registered @ <40028100..40028500)
	peripheral: 'Ethernet_PTP' of type 'Ethernet', registered @ <40028700..40028B00)
	peripheral: 'FLASH' of type 'FLASH', registered @ <40023C00..40024000), with interrupts: 'FLASH_IRQ' @ 4 
	peripheral: 'FSMC' of type 'FSMC', registered @ <A0000000..A0000400), with interrupts: 'FSMC_IRQ' @ 48 
	peripheral: 'GPIOA' of type 'GPIO', registered @ <40020000..40020400)
	peripheral: 'GPIOB' of type 'GPIO', registered @ <40020400..40020800)
	peripheral: 'GPIOC' of type 'GPIO', registered @ <40020800..40020C00)
	peripheral: 'GPIOD' of type 'GPIO', registered @ <40020C00..40021000)
	peripheral: 'GPIOE' of type 'GPIO', registered @ <40021000..40021400)
	peripheral: 'GPIOF' of type 'GPIO', registered @ <40021400..40021800)
	peripheral: 'GPIOG' of type 'GPIO', registered @ <40021800..40021C00)
	peripheral: 'GPIOH' of type 'GPIO', registered @ <40021C00..40022000)
	peripheral: 'GPIOI' of type 'GPIO', registered @ <40022000..40022400)
	peripheral: 'HASH' of type 'HASH', registered @ <50060400..50060800), with interrupts: 'HASH_RNG_IRQ' @ 80 
	peripheral: 'I2C1' of type 'I2C', registered @ <40005400..40005800), with interrupts: 'I2C1_EV_IRQ' @ 31 , 'I2C1_ER_IRQ' @ 32 
	peripheral: 'I2C2' of type 'I2C', registered @ <40005800..40005C00), with interrupts: 'I2C2_EV_IRQ' @ 33 , 'I2C2_ER_IRQ' @ 34 
	peripheral: 'I2C3' of type 'I2C', registered @ <40005C00..40006000), with interrupts: 'I2C3_EV_IRQ' @ 72 , 'I2C3_ER_IRQ' @ 73 
	peripheral: 'I2S2ext' of type 'SPI', registered @ <40003400..40003800)
	peripheral: 'I2S3ext' of type 'SPI', registered @ <40004000..40004400)
	peripheral: 'IWDG' of type 'IWDG', registered @ <40003000..40003400)
	peripheral: 'NVIC' of type 'NVIC', registered @ <E000E000..E000F001)
	peripheral: 'OTG_FS_DEVICE' of type 'USB_OTG_FS', registered @ <50000800..50000C00)
	peripheral: 'OTG_FS_GLOBAL' of type 'USB_OTG_FS', registered @ <50000000..50000400), with interrupts: 'OTG_FS_WKUP_IRQ' @ 42 , 'OTG_FS_IRQ' @ 67 
	peripheral: 'OTG_FS_HOST' of type 'USB_OTG_FS', registered @ <50000400..50000800)
	peripheral: 'OTG_FS_PWRCLK' of type 'USB_OTG_FS', registered @ <50000E00..50001200)
	peripheral: 'OTG_HS_DEVICE' of type 'USB_OTG_HS', registered @ <40040800..40040C00)
	peripheral: 'OTG_HS_GLOBAL' of type 'USB_OTG_HS', registered @ <40040000..140000400), with interrupts: 'OTG_HS_EP1_OUT_IRQ' @ 74 , 'OTG_HS_EP1_IN_IRQ' @ 75 , 'OTG_HS_WKUP_IRQ' @ 76 , 'OTG_HS_IRQ' @ 77 
	peripheral: 'OTG_HS_HOST' of type 'USB_OTG_HS', registered @ <40040400..40040800)
	peripheral: 'OTG_HS_PWRCLK' of type 'USB_OTG_HS', registered @ <40040E00..40080000)
	peripheral: 'PWR' of type 'PWR', registered @ <40007000..40007400), with interrupts: 'PVD_IRQ' @ 1 
	peripheral: 'RCC' of type 'RCC', registered @ <40023800..40023C00), with interrupts: 'RCC_IRQ' @ 5 
	peripheral: 'RNG' of type 'RNG', registered @ <50060800..50060C00), with interrupts: 'HASH_RNG_IRQ' @ 80 
	peripheral: 'RTC' of type 'RTC', registered @ <40002800..40002C00), with interrupts: 'RTC_WKUP_IRQ' @ 3 , 'RTC_Alarm_IRQ' @ 41 
	peripheral: 'SDIO' of type 'SDIO', registered @ <40012C00..40013000), with interrupts: 'SDIO_IRQ' @ 49 
	peripheral: 'SPI1' of type 'SPI', registered @ <40013000..40013400), with interrupts: 'SPI1_IRQ' @ 35 
	peripheral: 'SPI2' of type 'SPI', registered @ <40003800..40003C00), with interrupts: 'SPI2_IRQ' @ 36 
	peripheral: 'SPI3' of type 'SPI', registered @ <40003C00..40004000), with interrupts: 'SPI3_IRQ' @ 51 
	peripheral: 'SYSCFG' of type 'SYSCFG', registered @ <40013800..40013C00)
	peripheral: 'TIM1' of type 'TIM', registered @ <40010000..40010400), with interrupts: 'TIM1_BRK_TIM9_IRQ' @ 24 , 'TIM1_UP_TIM10_IRQ' @ 25 , 'TIM1_TRG_COM_TIM11_IRQ' @ 26 , 'TIM1_CC_IRQ' @ 27 
	peripheral: 'TIM10' of type 'TIM', registered @ <40014400..40014800), with interrupts: 'TIM1_UP_TIM10_IRQ' @ 25 
	peripheral: 'TIM11' of type 'TIM', registered @ <40014800..40014C00), with interrupts: 'TIM1_TRG_COM_TIM11_IRQ' @ 26 
	peripheral: 'TIM12' of type 'TIM', registered @ <40001800..40001C00), with interrupts: 'TIM8_BRK_TIM12_IRQ' @ 43 
	peripheral: 'TIM13' of type 'TIM', registered @ <40001C00..40002000), with interrupts: 'TIM8_UP_TIM13_IRQ' @ 44 
	peripheral: 'TIM14' of type 'TIM', registered @ <40002000..40002400), with interrupts: 'TIM8_TRG_COM_TIM14_IRQ' @ 45 
	peripheral: 'TIM2' of type 'TIM', registered @ <40000000..40000400), with interrupts: 'TIM2_IRQ' @ 28 
	peripheral: 'TIM3' of type 'TIM', registered @ <40000400..40000800), with interrupts: 'TIM3_IRQ' @ 29 
	peripheral: 'TIM4' of type 'TIM', registered @ <40000800..40000C00), with interrupts: 'TIM4_IRQ' @ 30 
	peripheral: 'TIM5' of type 'TIM', registered @ <40000C00..40001000), with interrupts: 'TIM5_IRQ' @ 50 
	peripheral: 'TIM6' of type 'TIM', registered @ <40001000..40001400), with interrupts: 'TIM6_DAC_IRQ' @ 54 
	peripheral: 'TIM7' of type 'TIM', registered @ <40001400..40001800), with interrupts: 'TIM7_IRQ' @ 55 
	peripheral: 'TIM8' of type 'TIM', registered @ <40010400..40010800), with interrupts: 'TIM8_BRK_TIM12_IRQ' @ 43 , 'TIM8_UP_TIM13_IRQ' @ 44 , 'TIM8_TRG_COM_TIM14_IRQ' @ 45 , 'TIM8_CC_IRQ' @ 46 
	peripheral: 'TIM9' of type 'TIM', registered @ <40014000..40014400), with interrupts: 'TIM1_BRK_TIM9_IRQ' @ 24 
	peripheral: 'UART4' of type 'USART', registered @ <40004C00..40005000), with interrupts: 'UART4_IRQ' @ 52 
	peripheral: 'UART5' of type 'USART', registered @ <40005000..40005400), with interrupts: 'UART5_IRQ' @ 53 
	peripheral: 'USART1' of type 'USART', registered @ <40011000..40011400), with interrupts: 'USART1_IRQ' @ 37 
	peripheral: 'USART2' of type 'USART', registered @ <40004400..40004800), with interrupts: 'USART2_IRQ' @ 38 
	peripheral: 'USART3' of type 'USART', registered @ <40004800..40004C00), with interrupts: 'USART3_IRQ' @ 39 
	peripheral: 'USART6' of type 'USART', registered @ <40011400..40011800), with interrupts: 'USART6_IRQ' @ 71 
	peripheral: 'WWDG' of type 'WWDG', registered @ <40002C00..40003000), with interrupts: 'WWDG_IRQ' @ 0 

