# GENIminiprojectCS655

echoclient.py - code for the master
echoserver.py - code for each individual worker

How to run:
  1. Get echoserver.py on each worker machine
  2. get echoclient.py on the master machine
  3. On each worker machine:
    a. adjust IP to worker machine IP in echoserver.py (or just use local for local testing)
    b. open terminal and navigate to echoserver.py. Run the following commandline: python echoserver.py <port_num>
    c. update echoclient.py on master machine with ip and port num
  4. Once all worker machines are up and running
  5. Navigate to echoclient.py on master machine, run: python echoclient.py
  6. enter in the md5 hash of the passcode you would like to be solved, and press enter
    
