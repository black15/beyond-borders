import Image from 'next/image'
import Link from 'next/link'
import React from 'react'

type Props = {}

const Header = (props: Props) => {
  return (
	<nav className="container mx-auto absolute left-0 right-0 top-0 z-10 w-full px-12 md:w-3/4">
		<div className="mx-auto px-4">
			<div className="flex justify-between">
				<div className="flex space-x-7">
					<div>
						<Link href="/" className="flex items-center py-4 px-2">
							{/* <Image src="" alt="Logo" width={50} height={50} className="h-8 w-8 mr-2" unoptimized /> */}
							<h1 className="text-gray-100 text-2xl font-pacifico">BeyondBRDR</h1>
						</Link>
					</div>
					<div className="hidden md:flex items-center space-x-1">
						<Link href="" className="py-4 px-2 text-rose-600 border-b-4 border-rose-600 font-semibold ">Home</Link>
						<Link href="" className="py-4 px-2 text-gray-100 font-semibold hover:text-rose-600 transition duration-300">Services</Link>
						<Link href="" className="py-4 px-2 text-gray-100 font-semibold hover:text-rose-600 transition duration-300">About</Link>
						<Link href="" className="py-4 px-2 text-gray-100 font-semibold hover:text-rose-600 transition duration-300">Contact Us</Link>
					</div>
				</div>
				<div className="hidden md:flex items-center space-x-3 ">
					<Link href="" className="py-2 px-2 font-medium text-gray-100 rounded hover:bg-rose-600 hover:text-white transition duration-300">Log In</Link>
					<Link href="" className="py-2 px-2 font-medium text-white bg-rose-600 rounded hover:bg-rose-600 transition duration-300">Sign Up</Link>
				</div>
				<div className="md:hidden flex items-center">
					<button className="outline-none mobile-menu-button">
					<svg className=" w-6 h-6 text-gray-500 hover:text-green-500 "
						x-show="!showMenu"
						fill="none"
						strokeLinecap="round"
						strokeLinejoin="round"
						strokeWidth="2"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path d="M4 6h16M4 12h16M4 18h16"></path>
					</svg>
				</button>
				</div>
			</div>
		</div>
		<div className="hidden mobile-menu">
			<ul className="">
				<li className="active"><Link href="index.html" className="block text-sm px-2 py-4 text-white bg-green-500 font-semibold">Home</Link></li>
				<li><Link href="#services" className="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">Services</Link></li>
				<li><Link href="#about" className="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">About</Link></li>
				<li><Link href="#contact" className="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">Contact Us</Link></li>
			</ul>
		</div>
	</nav>
  )
}

export default Header