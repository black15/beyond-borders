/* eslint-disable react/no-unescaped-entities */
import React from 'react'
import Item from './Item'

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
	items: [
	{
		name: string,
		slug: string,
		image: string,
		description: string,
		requester: Author,
		category: Category,
	}
	],
}

const Items = ({items}: Props) => {
  return (
	 <div className='container mx-auto w-full md:w-3/4'>
		<div className="flex flex-col items-center space-y-4 mt-24">
			<h1 className="text-3xl text-gray-800 font-bold font-poppins text-center">
				RECENT REQUESTED ITEMS
			</h1>
			<p className="max-w-xl text-gray-700 font-poppins text-center">
				Contact the item's Requester to discuss and know more about the item.
			</p>
		</div>
		<div className="flex flex-row flex-wrap items-center justify-center md:justify-start my-16">
			{items.map(item => (
				<Item key={item.slug} name={item.name} slug={item.slug} image={item.image} description={item.description} requester={item.requester} category={item.category} />
			))}
		</div>
	 </div>
  )
}

export default Items