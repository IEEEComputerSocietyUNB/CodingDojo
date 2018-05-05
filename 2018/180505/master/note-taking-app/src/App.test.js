import React from 'react'
import { render, getByText } from 'react-testing-library'
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
})
