import React from 'react'
import { render, Simulate } from 'react-testing-library'
import 'dom-testing-library/extend-expect'
import App from './App'

describe('App', () => {
  let app

  beforeEach(() => {
    app = render(<App />)
  })

  it('renders without crashing', () => {
    const { container, getByText } = app
    expect(getByText('Welcome to React')).toMatchSnapshot()
  })

  it('makes it possible to write', () => {
    const { getByAltText } = app
    expect(getByAltText('note')).toMatchSnapshot()
  })

  it('show input value on screen', () => {
    const { getByAltText, container } = app
    const note = getByAltText('note')
    
    expect(container.querySelector('.shownotes')).toMatchSnapshot()
    note.value = "potato"
    Simulate.change(note)

    expect(container.querySelector('.shownotes')).toHaveTextContent('potato')
  })



})
