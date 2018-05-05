import React from 'react'
import { render, Simulate } from 'react-testing-library'

import NoteList from './NoteList'

describe('NoteList', () => {
  let list

  beforeEach(() => {
    list = render(<NoteList />)
  })

  it('lets me create a new note', () => {
    const { container, getByText, getByLabelText } = list

    expect(container.querySelectorAll('.note').length).toBe(1)

    Simulate.click(getByText('new note'))

    expect(container.querySelectorAll('.note').length).toBe(2)
  })
})
