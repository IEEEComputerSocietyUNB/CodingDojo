import React, { Component } from 'react'
import Note from './Note'
import ShowNotes from './ShowNotes'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <Note />
        <ShowNotes />
      </div>
    )
  }
}

export default App
