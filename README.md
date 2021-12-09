# GENIminiprojectCS655

api/echoclient.py - code for the master
api/echoserver.py - code for each individual worker

How to run:
  1. Login to the master node and every worker node and clone repo one very master and worker node
  2. On the master machine:<br />
    a. run the setup shell file to download all necessary dependencies (node and flask)<br />
    b. if shell stalls on installing nodejs, exit out, relog in, and follow rest of the commands in shell file manually<br />
    c. run `npm start` on root<br />
    d. open new terminal and navigate to /api and run `source venv/bin/activate` and run `flask run`<br />
    e. navigate to http://204.102.244.53:3000/ on a local browser<br />
  3. On every worker machine:<br />
    a. navigate to repo/api folder and run "python3 echoserver.py 6000x", where x = 0, 1, 2, 3 for each of the 4 worker nodes <br />
    b. They should all show the following prompt
  5. Once all worker machines are up and running, and master webpage is working:<br />
    a. go to page opened in step 1e, enter in a valid md5 hash for a 5 character passcode, and an integer between 1-4 for the number of workers and hit the red button<br />
    b. While running, change the number of workers with the blue button. it is important not to hit the red button until the job is completely done<br />
    c. A job will finish when all workers return to "waiting for connection"<br />
  6. the solution will be displayed on the webpage<br />
    
