# Centralized server: keeps track of which clients are connected and storing what files.
In other words, the application will need a server have a feature of knowing the lively
connecting clients and the files that they publish on the server.
Client-server interaction :
• A client informs the server as to what files are contained in its local repository but
does not actually transmit file data to the server. This means clients will announce the
server the location or name of the file that he/she is keeping on his/her own computer.
They cannot upload the whole file data on to the server in this app.
• When a client requires a file that does not belong to its repository, a request is sent
to the server. The server identifies some other clients who store the requested file and
sends their identities to the requesting client. The client will select an appropriate
source node and the file is then directly fetched by the requesting client from the node
that has a copy of the file without requiring any server intervention. This mean client
will have the right to choose any available peer to get the file downloading.
Multithreading code : Multiple clients could be downloading different files from a target
client at a given point in time. This shown that the each comming request should be assigned
to a single thread to run their own downloading process or in others word, the client code
will be multithreaded.
Client’s command-shell interpreter :
• publish lname fname : On the client’s computer, the file has the original name is
lname, then they want to publish their file to the server with another file name fname.
Another client can ask for fetching the file with name is fname.
• fetch fname : When a client want to download the file with the name fname, they
ask for the server who is keeping this file, the server then return a list of available
peers for the client to contact and download.
Server’s command-shell interpreter :
• discover hostname : discover the list of local files of the host named hostname.
The server can keep track all published files of the client name "hostname".
• ping hostname : live check the host named hostname. The server can see if the
client name "hostname" are still connecting with the server or not.
In this implementation, we choose Python as the programming language with support
library "Tkinter" to make the GUI (Graphic User Interface).
