import React from 'react';
import PropTypes from 'prop-types';

const Guest = props => 
 
  <li>
    <span>{props.name}</span>
      <label>
        <input 
          type="checkbox" 
          checked={props.isConfirmed} 
          onChange={props.handleConfirmation}
        /> Confirmed
      </label>
      <button>edit</button>
      <button>remove</button>
  </li>

Guest.PropTypes = {
  name: PropTypes.string,
  isConfirmed: PropTypes.bool,
  handleConfirmation: PropTypes.func
}

export default Guest;