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
      nodeValue: ''
    }

    this.handleHashChange = this.handleHashChange.bind(this);
    this.handleNodeChange = this.handleNodeChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleHashChange(event) {
    this.setState({hashValue: event.target.value})
  }

  handleNodeChange(event) {
    this.setState({nodeValue: event.target.value})
  }

  handleSubmit(event) {
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
            <form onSubmit={this.handleSubmit}>
              <label>
                MD5 hash: 
                <input type="text" name="hashLabel" size='28' value={this.state.hashValue} onChange={this.handleHashChange} />
              </label>
              <label>
                Number of worker nodes:
                <input type="text" name="nodeLabel" size='1' value={this.state.nodeLabel} onChange={this.handleNodeChange} />
              </label>
              <input type="submit" value="Submit" />
            </form>
          </div>
        </header>
      </div>
    );
  }
}

export default App;
