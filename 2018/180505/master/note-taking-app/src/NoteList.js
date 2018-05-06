import React, { Component } from 'react'

export default class NoteList extends Component {
  state = {
    selected: [],
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
    this.props.removeNotes(this.state.selected)
    this.setState({
      selected: [],
    })
  }

  current = index => index === this.props.current ? 'current' : ''

  limit = (content) => {
    if (content.length > 30) {
      return `${content.slice(0, 30)}...`
    }

    return content 
  }

  render() {
    return (
      <div className="NoteList">
        <div className="toolbar">
          <button onClick={this.props.addNote}>
            new note
          </button>
          <button onClick={this.removeNotes}>
            remove selected notes
          </button>
        </div>

        <ul className="list">
          {this.props.list.map((note, index) => (
            <li
              className={`note ${this.current(index)}`} key={`${note}-${index}`}
              onClick={() => this.props.changeSelection(index)}
            >
              <input
                type="checkbox"
                alt={`remove note #${index + 1}`}
                checked={this.isNoteSelected(index)}
                onClick={() => this.toggleNote(index)}
              />
              <span className="content">
                {this.limit(note)}
              </span>
            </li>
          ))}
        </ul>
      </div>
    )
  }
}
