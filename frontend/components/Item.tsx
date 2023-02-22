import Image from 'next/image'
import Link from 'next/link'
import React from 'react'
import jwt_decode from 'jwt-decode'
import Cookies from 'js-cookie'

interface Author {
	id: number,
	email: string,
	username: string,
	author_name: string,
	role: number,
}
interface Category {
	id: number,
	name: string,
	slug: string,
	image?: string
}
interface Props {
	name: string,
	slug: string,
	image: string,
	description: string,
	requester: Author,
	category: Category,
}

const Item = ({name, slug, image, description, category, requester}: Props) => {	

	// const token = Cookies.get('access_token') || null
	// console.log('ff', token);
	
  	return (
	 	<div className='flex flex-col items-center justify-center m-3 p-3 border rounded'>
			<Link href={`/item/${slug}`} className='w-48 h-48'>
				<Image
					src={image}
					alt="Item's Image"
					width={200}
					height={200}
				/>
			</Link>
			<div className="w-full text-center">
				<h2 className="max-w-md text-gray-800 text-lg font-medium font-poppins">{name}</h2>
				<Link href={`/user/${requester.username}`} className="max-w-md text-gray-700 font-poppins">{requester.author_name}</Link>
			</div>
		</div>
  )
}

export default Item