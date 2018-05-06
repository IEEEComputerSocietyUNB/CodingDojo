import React, { Component } from 'react'
import Note from './Note'
import NoteList from './NoteList'

class App extends Component {
  state = {
    noteList: [
      'my first note',
    ],
    current: 0,
  }

  getCurrentNote = () => {
    const { noteList, current } = this.state

    return noteList[current]
  }

  handleChange = (event) => {
    const { noteList, current } = this.state

    this.setState({
      noteList: [...noteList.slice(0, current), event.target.value, ...noteList.slice(current + 1)]
    })
  }

  removeNotes = (notesToBeRemoved) => {
    this.setState(({ noteList, current }) => ({
      noteList: noteList.filter((note, index) => !notesToBeRemoved.includes(index)),
      current: 0,
    }))
  }

  addNote = () => {
    this.setState(({ noteList }) => ({
      noteList: [...noteList, noteList.length],
      current: noteList.length,
    }))
  }

  changeSelection = (index) => {
    this.setState({
      current: index,
    })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <div className="App-intro">
          <NoteList
            list={this.state.noteList}
            addNote={this.addNote}
            removeNotes={this.removeNotes}
            changeSelection={this.changeSelection}
            current={this.state.current}
          />
          <Note
            note={this.getCurrentNote()}
            onNoteEdit={this.handleChange}
          />
        </div>
      </div>
    )
  }
}

export default App
