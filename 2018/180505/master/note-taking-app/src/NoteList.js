import React, { Component } from 'react'

export default class NoteList extends Component {
  state = {
    list: [
      'my first note',
    ],
    selected: []
  }

  addNote = () => {
    this.setState({
      list: [...this.state.list, this.state.list.length]
    })
  }

  toggleNote = (index) => {
    if (this.isNoteSelected(index)) {
      this.setState({
        selected: this.state.selected.filter(i => i !== index)
      })
    } else {
      this.setState({
        selected: [...this.state.selected, index]
      })
    }
  }

  isNoteSelected = (index) => {
    return this.state.selected.includes(index)
  }

  removeNotes = () => {
    this.setState(state => ({
      list: state.list.filter((note, index) => !state.selected.includes(index)),
      selected: [],
    }))
  }

  render() {
    return (
      <div className="NoteList">
        <div className="toolbar">
          <button onClick={this.addNote}>
            new note
          </button>
          <button onClick={this.removeNotes}>
            remove selected notes
          </button>
        </div>

        <ul className="list">
          {this.state.list.map((note, index) => (
            <li className="note" key={`${note}-${index}`}>
              <input
                type="checkbox"
                alt={`remove note #${index + 1}`}
                checked={this.isNoteSelected(index)}
                onClick={() => this.toggleNote(index)}
              />
              {note}
            </li>
          ))}
        </ul>
      </div>
    )
  }
}
