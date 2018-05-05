import React from 'react'
import {
  render,
  Simulate,
} from 'react-testing-library'

import Note from './Note'

describe('Note', () => {
  let input

  beforeEach(() => {
    const { container, getByPlaceholderText } = render(<Note />)
    input = getByPlaceholderText('Your note goes here')
  })

  it('renders a input field with placeholder `Your note goes here`', () => {
    expect(input).toMatchSnapshot()
  })

  it('allows me to type into the input', () => {
    input.value = 'potato'
    Simulate.change(input)
    expect(input).toMatchSnapshot()
  })
})
