import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import logo from './logo.svg';
import passkey from './passkey.svg'
import './App.css';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      hashValue: '',
      nodeValue: '',
      currentTime: 0
    }

    this.handleHashChange = this.handleHashChange.bind(this);
    this.handleNodeChange = this.handleNodeChange.bind(this);
    this.handleSubmit1 = this.handleSubmit1.bind(this);
    this.handleSubmit2 = this.handleSubmit2.bind(this);
  }

  setCurrentTime(time) {
    this.setState({currentTime: time})
  }

  useEffect() {
    fetch('/time').then(res => res.json()).then(data => {
      this.setCurrentTime(data.time);
    });
  };

  InsertArticle(body){
    return fetch(`http://localhost:3000/time`,{
        'method':'POST',
        headers : {
          'Content-Type':'application/json'
        },
    body:JSON.stringify(body)
  })
  .then(response => response.json())
  .catch(error => console.log(error))
  }

  insertArticle(hash, num) {
    this.InsertArticle({hash,num})
    // .then((response) => props.insertedArticle(response))
    // .catch(error => console.log('error',error))
  }

  handleHashChange(event) {
    this.setState({hashValue: event.target.value})
  }

  handleNodeChange(event) {
    this.setState({nodeValue: event.target.value})
  }

  handleSubmit1(event) {
    event.preventDefault();
    this.changeNumber(this.state.nodeValue);
    // this.useEffect
  }

  changeNumber(num) {
    this.ChangeNumber({num})
    // .then((response) => props.insertedArticle(response))
    // .catch(error => console.log('error',error))
  }

  ChangeNumber(body){
    return fetch(`http://localhost:3000/change`,{
        'method':'POST',
        headers : {
          'Content-Type':'application/json'
        },
    body:JSON.stringify(body)
  })
  .then(response => response.json())
  .catch(error => console.log(error))
  }

  handleSubmit2(event) {
    // Regular expression to check if string is a MD5 hash
    const regexExp = /^[a-f0-9]{32}$/gi;

    if (!(regexExp.test(this.state.hashValue))) {
      alert('INVALID HASH: Please enter a valid MD5 hash.')
      event.preventDefault();
    } else if (isNaN(parseInt(this.state.nodeValue))) {
      alert('INVALID NUMBER: Please enter an integer for worker nodes input.')
      event.preventDefault();
    } else {
      alert('A hash of <' + this.state.hashValue + '> was submitted with ' + this.state.nodeValue + ' worker nodes.');
      alert('> this is where i would send this tuple to master server: ' + [this.state.hashValue, this.state.nodeValue]);
      event.preventDefault();
    }

    this.insertArticle(this.state.hashValue, this.state.nodeValue);

    this.useEffect();
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={passkey} className="App-logo" alt="logo" />
          {/* <p>
            Edit <code>src/App.js</code> and save to reload.
          </p> */}
          <h1>Passcracker</h1>
          {/* <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a> */}
          <div className="Form">
            {/* <p>test</p> */}
            <form>
              <label>
                MD5 hash: 
                <input type="text" name="hashLabel" size='28' value={this.state.hashValue} onChange={this.handleHashChange} />
              </label>
              <label>
                Number of worker nodes:
                <input type="text" name="nodeLabel" size='1' value={this.state.nodeLabel} onChange={this.handleNodeChange} />
              </label>
              <button id="buttonWork" type="submit" name="submitWork" onClick={this.handleSubmit1}>Change number of workers</button>
              <button id="buttonFull" type="submit" name="submitFull" onClick={this.handleSubmit2}>Submit job</button>
            </form>
            <p>The current time is {this.state.currentTime}.</p>
          </div>
        </header>
      </div>
    );
  }
}

export default App;
