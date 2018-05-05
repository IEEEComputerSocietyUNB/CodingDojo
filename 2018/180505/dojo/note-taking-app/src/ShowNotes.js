import React, { Component } from 'react'
export default class ShowNotes extends Component {
  render() { return (
    <ul>
      <input alt="shownotes" value={this.props.value}/>  
        {/* {this.props.listaRecados.map(i => )} */}
    </ul>
  );
  }
}
