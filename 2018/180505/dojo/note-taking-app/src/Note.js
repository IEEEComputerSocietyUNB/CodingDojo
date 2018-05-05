import React, { Component } from 'react'

export default class Note extends Component {
  render() {  return (
    <p>
      <input type="text"
        alt="note"
        value={this.props.value}
        onChange={this.props.handleChange}
      />
    </p>
  );
  }
}
