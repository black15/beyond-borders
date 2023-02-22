import { default as axios } from 'axios'

interface Credentials {
	email: string,
	password: string,
}

const DJANGO_API: string = process.env.NEXT_PUBLIC_DJANGO_API_BASE_URL!

export const getAllItems = async () => {
	const res = await axios.get(`${DJANGO_API}/items`) 
	const data = await res.data

	return data
}

export const authUser = async (creds: Credentials) => {
	try {
		const res = await axios.post(`${DJANGO_API}/auth/signin/`, creds)
		const data = await res.data
		return data

	} catch (error: any) {
		return error.response
	}
	
}