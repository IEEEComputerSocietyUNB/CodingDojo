import React, { Component } from 'react'

export default class Note extends Component {
  state = {
    content: ''
  }

  handleChange = (event) => {
    this.setState({
      content: event.target.value
    })
  }

  render() {
    return (
      <div className="Note">
        <input
          type="text"
          value={this.state.content}
          onChange={this.handleChange}
          placeholder="Your note goes here"
        />
      </div>
    )
  }
}
