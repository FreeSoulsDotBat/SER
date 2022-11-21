import { View, Image } from 'react-native'

export const Header = () => {
	return (
		<View
			style={{
				backgroundColor: '#F6F6F6',
				height: 90,
				maxHeight: 90,
				width: '100%',
				justifyContent: 'center',
				alignItems: 'flex-start',
				paddingLeft: 20,
			}}>
			<Image
				style={{
					resizeMode: 'contain',
					maxHeight: '75%',
					width: '65%',
				}}
				source={require('../assets/extenseLogo.png')}
			/>
		</View>
	)
}
