import React from 'react';
import PropTypes from 'prop-types';
import Guest from './Guest';

const GuestList = props => 
  <ul>
    {props.guests.map((guest, index) => 
      <Guest 
        key={index} 
        name={guest.isConfirmed}
        isConfirmed={guest.isConfirmed}
      />
    )} 
  </ul>
GuestList.PropTypes = {
  guests: PropTypes.array
}

export default GuestList;