.MODEL small
.STACK 100h
.DATA
	a_count db 0		;������� ��������� ������
	nln db '', 10,13,'$' 	;������� ������
.CODE
start:
	mov ax, @data
	mov ds, ax
	mov si,0 		
	mov cx, offset exit		
	sub cx, offset start	;���������� ������ ������

lab1:
	mov dl, cs:[si]

	mov bl, dl    
	shr dl, 04		;������������ ����� �� 4 ������� ������
	add dl, 30h
	cmp dl, 39h		;���������� � 9
	jle m1
	add dl, 7h
	
m1:	mov ah, 02h		;������� ������� �����
	int 21h
	
	mov dl, bl
	and dl, 0Fh		;�������� ������� �����
	add dl, 30h
	cmp dl, 39h
	jle m2
	add dl, 7h

m2:	mov ah, 02h		;������� ������� �����
	int 21h

	inc si
	mov dl, 20h		;������� ������	
	mov al, 02h
	int 21h
	
	inc a_count		;����������� ������� ������
	cmp a_count, 16		;���������� � 16
	jne m3			;���� �� �����, �� ��������� �� m2
	mov a_count, 0h		;����� �������� �������
	lea dx, nln		;� ��������� �� ����� ������
	mov ah, 09h
	int 21h
m3: loop lab1
	
	mov  AH,00     		;������� �����
   	int  16H       		;�������� �������
	cmp al, 0dh		;���������, ������ ������� Enter?
	je exit			;���� ��, �� �������

exit:
	mov ah, 05h		;��� ������ ����������� �� ������� ��������
	mov al, 00
	int 10h
	mov ax, 4c00h
	int 21h
END start
