package main

import (
    "fmt"
    "os"
    "log"
)

func main() {
	// Array helper
	numbers := [8]byte{ 128, 64, 32, 16, 8, 4, 2, 1 }
	// Polynom
	var poly byte = 0xD5
    // Open file for reading
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }

    b_init := make([]byte, 1)
    file.Read(b_init)
	log.Printf("%n", b_init[0])
    b_init[0] = b_init[0] ^ poly
    b_init[0] = b_init[0] << 1
    for true {
        b := make([]byte, 1)
        _, err := file.Read(b)
        if err != nil {
			for i := 0; i < 8; i++ {
			    b_init[0] = b_init[0] ^ poly
				b_init[0] = b_init[0] << 1
			}
            fmt.Printf("CRC8 code is %n \n", b_init[0])
            break
        }
        for i := 0; i < 8; i++ {
            is_one := b[0] & numbers[i]
            if is_one == 1 {
            	b_init[0] = b_init[0] + 1
			}
            b_init[0] = b_init[0] ^ poly
            b_init[0] = b_init[0] << 1
        }
    }
}
