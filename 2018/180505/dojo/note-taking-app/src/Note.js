import React, { Component } from 'react'

export default class Note extends Component {
  render() {  return (
    <div>
      <p>
        <input type="text"
          alt="note"
          value={this.props.value}
          onChange={this.props.handleChange}
        />
      </p>
      <button className="button-add-note" onClick={this.props.addNote}>Add Note</button>
    </div>
  );
  }
}
