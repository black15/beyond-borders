import { default as axios } from 'axios'

const DJANGO_API: string = process.env.NEXT_PUBLIC_DJANGO_API_BASE_URL!

export const getAllItems = async () => {
	const res = await axios.get(`${DJANGO_API}/items`) 
	const data = await res.data

	return data
}