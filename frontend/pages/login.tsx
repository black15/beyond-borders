import { SignInForm } from '@/components/AuthForm'
import React from 'react'

type Props = {}

const login = (props: Props) => {
  return (
	 <div className='h-48'>
		<SignInForm />
	 </div>
  )
}

export default login

