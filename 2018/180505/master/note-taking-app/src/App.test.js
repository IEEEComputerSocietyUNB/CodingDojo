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

  it('types into the input', () => {
    const { container } = app

    const input = container.querySelector('div.Note input')
    input.value = 'potato'
    Simulate.change(input)
    expect(input).toMatchSnapshot()
  })

  it('edits notes', () => {
    const { container } = app
    const note = container.querySelector('div.Note input')
    const noteList = container.querySelector('.NoteList ul')

    note.value = "My new value"
    Simulate.change(note)

    expect(noteList).toMatchSnapshot()
    expect(note).toMatchSnapshot()
  })

  it('creates new notes', () => {
    const { container, getByText } = app

    expect(container.querySelectorAll('li.note').length).toBe(1)

    Simulate.click(getByText('new note'))

    expect(container.querySelectorAll('li.note').length).toBe(2)
  })

  it('removes notes', () => {
    const { container, getByText, getByAltText } = app

    // adds 2 more, now we have 3 notes
    Simulate.click(getByText('new note'))
    Simulate.click(getByText('new note'))

    Simulate.click(getByAltText('remove note #2'))
    Simulate.click(getByText('remove selected notes'))

    expect(container.querySelectorAll('li.note').length).toBe(2)
  })
})
