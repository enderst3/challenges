import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className='header'>
        <h1>Scoreboard</h1>
        </div>
        <div className='players'>
          <div className='player'>
            <div className='player-name'>
              Todd
            </div>
            <div className='player-score'>
              <div className='counter'>
                <button className='counter-action minus'> - </button>
                <div className='counter-score'> 13 </div>
                <button className='counter-action plus'> + </button>
              </div>
            </div>
          </div>
          <div className='player'>
            <div className='player-name'>
              Johnny
            </div>
            <div className='player-score'>
              <div className='counter'>
                <button className='counter-action minus'> - </button>
                <div className='counter-score'> 11 </div>
                <button className='counter-action plus'> + </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
/*
let PLAYERS = [
  {
    name: 'Todd',
    score: 13,
    id: 1
  },
  {
    name: 'Johnny',
    score: 9,
    id: 2
  },
  {
    name: 'Sally',
    score: 43,
    id: 3
  }
]

function Header(props) {
  return (
    <div className='header'>
      <h1>{props.title}</h1>
    </div>
  )
}

Header.propTypes = {
  title: React.PropTypes.string.isRequired,
};


function Player(props) {
  return (
    <div className='player'>
      <div className='player-name'>
        {props.name}
      </div>
      <div className='player-score'>
        <div className='counter'>
          <button className='counter-action minus'> - </button>
          <div className='counter-score'> {props.score} </div>
          <button className='counter-action plus'> + </button>
        </div>
      </div>
    </div>
  )
}

Player.propTypes = {
  name: React.PropTypes.string.isRequired,
  score: React.PropTypes.number.isRequired,
}


function Application(props) {
  return (
    <div className='scoreboard'>
        <Header title={props.title} />
      <div className='players'>
        {props.players.map(function(player) {
          return <Player name={player.name} score={player.score} key={player.id} />
        })}
      </div>
    </div>
  );
}


Application.propTypes = {
  title: React.PropTypes.string,
  players: React.PropTypes.array,
  id: React.PropTypes.number,
};

Application.defaultProps = {
  title: 'Scoreboard'
}
ReactDOM.render(<Application players={PLAYERS}/>, document.getElementById('container'));

*/