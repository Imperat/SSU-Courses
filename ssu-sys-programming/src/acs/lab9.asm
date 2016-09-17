        .model small
        .stack 100h
        .386
        .data
        .code

asc     proc
        add     dl, 30h
        cmp     dl, 39h
        jle     l1
        add     dl, 07h
l1:     ret
asc     endp

setpg   proc
        pusha
        mov     ah, 05
        mov     al, 1
        int     10h    
        popa
        ret
setpg   endp

retpg   proc
        pusha
        mov     ah, 05
        mov     al, 0
        int     10h     
        popa
        ret
retpg   endp

start:  mov     ax, @data
        mov     ds, ax
 
        mov     ax, 0B900h
        mov     es, ax

        mov     cx, offset endm
        sub     cx, offset start
 
        call    setpg
                
        xor     di, di
l2:     xor     ax, ax
        mov     al, cs:[di]
        mov     bl, 16
        div     bl
        mov     dl, al
        call    asc
        mov     es:[di], dl
        inc     di
        mov     es:[di], 0fh
        inc     di
        mov     dl, ah
        call    asc
        mov     es:[di], dl
        inc     di
        mov     es:[di], 0fh
        inc     di
        loop    l2

        mov     ah, 01h
        int     21h
        call    retpg

        mov     ax, 4C00h
endm:   int     21h
 
        end     start