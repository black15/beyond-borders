import { authUser } from '@/services';
import { loginuser, selectToken } from '@/store/auth/authSlice';
import { useDispatch, useSelector } from 'react-redux';


export const SignInForm = () => {

	const dispatch = useDispatch()
	const token = useSelector(selectToken)

	const handleSubmit = (event: any) => {
		event.preventDefault()
		const email: string = event.target.email.value
		const password: string = event.target.password.value

		// authUser({email, password})
		// .then(res => {
		// 	console.log('RESPONSE : ', res);	
		// })
		// .catch(err => {
		// 	console.log('err');
		// })
		dispatch(loginuser({email, password}))
	}
   return (
     	<div className="flex flex-col items-center justify-center">
			token{token}
			<form onSubmit={handleSubmit}>
				<label htmlFor="email">Email</label>
				<input
					id="email"
					name="email"
					type="text"
				/>
				<label htmlFor="password">Password</label>
				<input
					id="password"
					name="password"
					type="password"
				/>
				<button type="submit">Submit</button>
			</form>
		</div>
   );
};