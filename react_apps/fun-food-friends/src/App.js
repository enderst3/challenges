import React, { Component } from 'react';
import './App.css';
import firebase from './firebase'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentItem: '',
      username: '',
      items: []
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    this.setState({
      // the code in the brackets is used in place of username, or currentItem
      [e.target.name]: e.target.value
    })
  }

  handleSubmit(e) {
    // prevents page from refreshing on submit
    e.preventDefault();
    // tells db where we want to store items
    const itemsRef = firebase.database().ref('items')
    // each item we want to store in items
    const item = {
      title: this.state.currentItem,
      user: this.state.username
    }
    // pushes the item to the items db
    itemsRef.push(item)
    // resets state back to empty strings so more can be added
    this.setState({
      currentItem: '',
      username: ''
    })
  }

  componentDidMount() {
    const itemsRef = firebase.database().ref('items')
    // value is a custom event lister.  will keep the page updated
    itemsRef.on('value', (snapshot) => {
      console.log(snapshot.val())
      let items = snapshot.val()
      let newState = []
      for (let item in items) {
        newState.push({
          id: item,
          title: items[item].title,
          user: items[item].user
        })
      }
      this.setState({
        items: newState
      })
    })
  
  }

  removeItem(itemId) {
    const itemRef = firebase.database().ref(`/items/${itemId}`)
    itemRef.remove()
  }

  render() {
    return (
      <div className="App">
        <header>
          <div className='wrapper'>
            <h1>Fun Food Friends</h1>
          </div>
        </header>
        <div className="container">
          <section className='add-item'>
            <form
              onSubmit={this.handleSubmit}
            >
              <input
                type='text'
                name='username'
                placeholder="What's your name?"
                onChange={this.handleChange}
                value={this.state.username}
              />
              <input type='text'
                name='currentItem'
                placeholder="What are you bringing?"
                onChange={this.handleChange}
                value={this.state.currentItem}
              />
              <button>Add Item</button>
            </form>
          </section>
          <section className='display-item'>
            <div className='wrapper'>
              <ul>
                {this.state.items.map((item) => {
                  return (
                    <li key={item.id}>
                      <h3>{item.title}</h3>
                      <p>Brought by: {item.user}</p>
                      <button
                        onClick={() => this.removeItem(item.id)}
                      >
                        Remove item
                      </button>
                    </li>
                  )
                })}
              </ul>
            </div>
          </section>
        </div>
      </div>
    );
  }
}

export default App;
