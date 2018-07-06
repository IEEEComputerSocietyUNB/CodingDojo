import React, { Component } from 'react'

export default class ShowNotes extends Component {
  render()
  {
    return (
      <ul>
        {this.props.listNotes.map((note,index) =>
          <li key={`potato-${index}`} className="shownotes">{ note }</li>
        )}
      </ul>
    )
  }
}
