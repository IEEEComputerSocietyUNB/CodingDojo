import React from 'react'
import { render, Simulate } from 'react-testing-library'

import NoteList from './NoteList'

describe('NoteList', () => {
  let list

  beforeEach(() => {
    list = render(<NoteList />)
  })

  it('lets me create a new note', () => {
    const { container, getByText } = list

    expect(container.querySelectorAll('.note').length).toBe(1)

    Simulate.click(getByText('new note'))

    expect(container.querySelectorAll('.note').length).toBe(2)
  })

  it('lets me remove notes', () => {
    const { container, getByText, getByAltText } = list

    // adds 2 more, now we have 3 notes
    Simulate.click(getByText('new note'))
    Simulate.click(getByText('new note'))

    Simulate.click(getByAltText('remove note #2'))
    Simulate.click(getByText('remove selected notes'))

    expect(container.querySelectorAll('.note').length).toBe(2)
  })
})
