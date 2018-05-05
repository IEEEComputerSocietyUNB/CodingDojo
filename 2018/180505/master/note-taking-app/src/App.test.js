import React from 'react'
import { render, getByText } from 'react-testing-library'
import App from './App'

describe('App', () => {
  it('renders without crashing', () => {
    const { container, getByText } = render(<App />)
    expect(getByText('Welcome to React')).toMatchSnapshot()
  })  
})
