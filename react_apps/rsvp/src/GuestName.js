import React from 'react';
import PropTypes from 'prop-types';


const GuestName = props => {
  if (props.isEditing) {
    return(
      <input
        type='text'
        value={props.children}
      />
    )
  }
  
  return (
    <span>
      {props.children}
    </span>
  )
}
 
GuestName.PropTypes = {
  isEditing: PropTypes.bool
}

export default GuestName;