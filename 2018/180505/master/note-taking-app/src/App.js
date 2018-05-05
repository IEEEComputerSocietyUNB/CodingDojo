import React, { Component } from 'react'
import Note from './Note'
import NoteList from './NoteList'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <div className="App-intro">
          <NoteList />
          <Note />
        </div>
      </div>
    )
  }
}

export default App
