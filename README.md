# GENIminiprojectCS655

api/echoclient.py - code for the master
api/echoserver.py - code for each individual worker

How to run:
  1. Clone repo one very master and worker node
  2. On the master machine:
    a. run the setup shell file to download all necessary dependencies (node and flask)
    b. if shell stalls on installing nodejs, exit out, relog in, and follow rest of the commands in shell file manually
    c. run `npm start` on root
    d. open new terminal and navigate to /api and run `source venv/bin/activate` and run `flask run`
    e. navigate to http://204.102.244.53:3000/ on a local browser
  3. On every worker machine, 
  4. Once all worker machines are up and running
  5. Navigate to echoclient.py on master machine, run: python echoclient.py
  6. enter in the md5 hash of the passcode you would like to be solved, and press enter
    
