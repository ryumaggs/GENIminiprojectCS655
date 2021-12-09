import React, {Component} from 'react'
import passkey from './passkey.svg'
import './App.css';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      hashValue: '',
      nodeValue: '',
      decryptedPass: ""
    }

    this.handleHashChange = this.handleHashChange.bind(this);
    this.handleNodeChange = this.handleNodeChange.bind(this);
    this.handleSubmit1 = this.handleSubmit1.bind(this);
    this.handleSubmit2 = this.handleSubmit2.bind(this);
  }

  setDecryptedPass(decryptedP) {
    this.setState({decryptedPass: decryptedP})
  }

  SendData(body){
    return fetch(`http://204.102.244.53:3000/decrypt`,{
        'method':'POST',
        headers : {
          'Content-Type':'application/json'
        },
    body:JSON.stringify(body)
  })
  .then(response => response.json())
  .then(data => {
    this.setDecryptedPass(data.dpass);
  })
  .catch(error => console.log(error))
  }

  sendData(hash, num) {
    this.SendData({hash,num})
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
    return fetch(`http://204.102.244.53:3000/change`,{
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
      // success
      event.preventDefault();
    }

    this.sendData(this.state.hashValue, this.state.nodeValue);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={passkey} className="App-logo" alt="logo" />
          <h1>Passcracker</h1>
          <div className="Form">
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
            <p>The decrypted password is: {this.state.decryptedPass}</p>
          </div>
        </header>
      </div>
    );
  }
}

export default App;
