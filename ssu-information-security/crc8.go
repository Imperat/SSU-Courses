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
	var r byte = 0
    // Open file for reading
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }

    b_init := make([]byte, 1)
    file.Read(b_init)
    b_init[0] = b_init[0] ^ poly
	fmt.Printf("%n \n", b_init[0])
    b_init[0] = b_init[0] << 1
    for true {
        b := make([]byte, 1)
        _, err := file.Read(b)
        if err != nil {
			for i := 0; i < 8; i++ {
			   b_init[0] = b_init[0] << 1
			   b_init[0] = b_init[0] ^ poly
			}
            break
        }
        for i := 0; i < 8; i++ {
			//b_init[0] = b_init[0] << 1
            is_one := b[0] & numbers[i]
            if is_one > 0 {
            	b_init[0] = b_init[0] + 1
			}
			// Add if statement
			r = (b_init[0] & 128) >> 7
			if r == 1 {
                b_init[0] = b_init[0] ^ poly
			}
			fmt.Printf("%n \n", b_init[0])
			b_init[0] = b_init[0] << 1
        }
    }
}
