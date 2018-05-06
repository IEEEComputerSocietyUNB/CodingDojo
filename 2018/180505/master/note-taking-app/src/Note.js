import React, { Component } from 'react'

export default class Note extends Component {
  render() {
    return (
      <div className="Note">
        <textarea
          type="text"
          value={this.props.note}
          onChange={this.props.onNoteEdit}
          placeholder="Your note goes here"
        />
      </div>
    )
  }
}
