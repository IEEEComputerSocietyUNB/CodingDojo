import React, { Component } from 'react'

export default class Note extends Component {
  render() {  return (
    <p>
        <label htmlFor={this.props.name}>Answer:</label>
        <input
          type="text"
          name={this.props.name}
          alt="note"
          value={this.props.value}
          onChange={this.props.handleChange}
        />
    </p>
  );
  }
}
