import React, { Component } from 'react'

export default class NoteList extends Component {
  state = {
    list: [
      'my first note',
    ]
  }

  addNote = () => {
    this.setState({
      list: [...this.state.list, '']
    })
  }

  render() {
    return (
      <div className="NoteList">
        <div className="toolbar">
          <button onClick={this.addNote}>
            new note
          </button>
        </div>

        <ul className="list">
          {this.state.list.map(note => (
            <li className="note" key={note}>
              {note}
            </li>
          ))}
        </ul>
      </div>
    )
  }
}
