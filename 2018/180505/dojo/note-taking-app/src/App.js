import React, { Component } from 'react'
import Note from './Note'
import ShowNotes from './ShowNotes'

class App extends Component {
  state = {
    value: '',
    listNotes: ['potato', 'oioi']
  }

  handleChange = (event) => {
    this.setState({
      value: event.target.value,
    })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <Note handleChange={this.handleChange} value={this.state.value} />
        <ShowNotes listNotes={this.state.listNotes} />
      </div>
    )
  }
}

export default App
