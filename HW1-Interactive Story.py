#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Jedsada Thavornfung, 1/19/23

choice1 = input('One day, you walk into the forest. There are THREE pathes you can choose. Which path would you choose: straight, left, or right?: ')

if(choice1.lower() == 'straight'):
    print('You chose to walk STRAIGHT into the forest. Now, you see a chest.')
    st1 = input('Would you open the chest: yes or no?: ')
    if(st1.lower() == 'yes'):
        print('You found a diamond in the chest.')
        st2 = input('Will you touch the diamond: yes or no?: ')
        st3 = input('Will you take the diamond with you: yes or no?: ')
        if(st2.lower() == 'yes' and st3.lower() == 'yes'):
            print('You take the diamond with you. Now, you see a scary demond came out from the chest asking you to return the diamond.')
            st4 = input('Will you return the diamond: yes or no?: ')
            if(st4.lower() == 'yes'):
                print('You decide to return back to the demond. And, the demond send you back home safety with $10,000 in your pocket.')
            elif(st4.lower() == 'no'):
                print('You got killed by the demon. Dead as hell!')
            else:
                print('INVALID. Please put the correct response.')
        elif(st2.lower() == 'no' and st3.lower() == 'yes'):
            print('You decided to take the diamond with you anyway. Now, you see a scary demond came out from the chest asking you to return the diamond.')
            st5 = input('Will you return the diamond: yes or no?: ')
            if(st5.lower() == 'yes'):
                print('You decide to return back to the demond. And, the demond send you back home safety with $10,000 in your pocket.')
            elif(st5.lower() == 'no'):
                print('You got killed by the demon. Dead as hell!')
            else:
                print('INVALID. Please put the correct response.')
        elif(st3.lower() == 'no'):
            print('You did not take the diamond and close the chest. Suddenly, the demond came out from the chest.')
            st6 = input('What would you do: fight or run?: ')
            if(st6.lower() == 'fight'):
                print('You immediately got killed by the demond. And being reincarnated as a worm in that forest.')
            elif(st6.lower() == 'run'):
                print('The demond somehow did not chase you. And, you safely escape from the forest.')
            else:
                print('INVALID. Please put the correct response.')
        else:
            print('INVALID. Please put the correct response.')
    elif(st1.lower() == 'no'):
        print('You did not open the chest(how boring). But, you somehow have an ability to change the weather.')
        st7 = input('Will you make it rain: yes or no?: ')
        st8 = input('Will you run or dance?: ')
        if(st7.lower() == 'yes' and st8.lower() == 'run'):
            print('You get what you wished for. It is now raining. Suddenly, you see the end of the forest.')
            st9 = input('Will you \'leave\' or \'stay\' in the forest?: ')
            if(st9.lower() == 'leave'):
                print('You safely returned home.')
            elif(st9.lower() == 'stay'):
                print('You stuck in the forest for the rest of your life!')
            else:
                print('INVALID. Please put the correct response.')
        elif(st7.lower() == 'yes' and st8.lower() == 'dance'):
            print('You get what you wished for. It is now raining. Suddenly, you see the end of the forest.')
            st10 = input('Will you \'leave\' or \'stay\' in the forest?: ')
            if(st10.lower() == 'leave'):
                print('You safely returned home.')
            elif(st10.lower() == 'stay'):
                print('You stuck in the forest for the rest of your life!')
            else:
                print('INVALID. Please put the correct response.')
        elif(st7.lower() == 'no'):
            print('You get what you wished for. There is no rain. Suddenly, you see the end of the forest.')
            st11 = input('Will you \'leave\' or \'stay\' in the forest?: ')
            if(st11.lower() == 'leave'):
                print('You safely returned home.')
            elif(st11.lower() == 'stay'):
                print('You stuck in the forest for the rest of your life!')
            else:
                print('INVALID. Please put the correct response.')
        else:
            print('INVALID. Please put the correct response.')
    else:
        print('INVALID. Please put the correct response.')

elif(choice1.lower() == 'left'):
    print('You chose to walk to the LEFT path and walk deeper into the forest. Now, you see a lion')
    lt1 = input('Would you \'run\' or \'fight\'?: ')
    if(lt1.lower() == 'run'):
        print('You manage to escape from the lion. However, you now see the witch in front of you. The witch will grant you 2 wishes.')
        lt2 = input('Wish 1 will make you escape the forest. Will you \'accept\' or \'deny\' the wish?: ')
        lt3 = input('Wish 2 will make you never hungry again. Will you \'accept\' or \'deny\' the wish?: ')
        if(lt2.lower() == 'accept' and lt3.lower() == 'accept'):
            print('You escaped from the forest. However, the witch would not give you the second wish unless you give her 5 years of your life span.')
            lt4 = input('Would you give the witch 5 years of your life span in exchange with the 2nd wish: yes or no?: ')
            if(lt4.lower() == 'yes'):
                print('You granted the second wish and never hungry again for the rest of your life...')
            elif(lt4.lower() == 'no'):
                print('You were not granted the second wish, but the witch is now mad and curse you to be single forever.')
            else:
                print('INVALID. Please put the correct response.')
        elif(lt2.lower() == 'accept' and lt3.lower() == 'deny'):
            print('You escaped from the forest. However, the witch ask you again if you want the second wish.')
            lt5 = input('Are you sure that you do not want the second wish: yes or no?: ')
            if(lt5.lower() == 'yes'):
                print('You do not want the second wish. However, the witch is now mad and curse you to be single forever.')
            elif(lt5.lower() == 'no'):
                print('You granted the second wish and never hungry again for the rest of your life...')
            else:
                print('INVALID. Please put the correct response.')
        elif(lt2.lower() == 'deny'):
            print('You stuck in the forest. The witch then ask you again if you truely do not want the forest.')
            lt6 = input('Are you sure that you do not want the leave the forest: yes or no?: ')
            if(lt6.lower() == 'yes'):
                print('You are now stuck in the forest forever. The witch is magically disappeared in front of your face.')
            elif(lt6.lower() == 'no'):
                print('You are now successfully escaped the forest. And, the witch is now out of your sight.')
            else:
                print('INVALID. Please put the correct response.')
        else:
            print('INVALID. Please put the correct response.')
    elif(lt1.lower() == 'fight'):
        print('You bravely fought the lion. However, since you do not have plot armor, you lose immediately. Just about when your soul abote to cross to the other side, The witch appear out of no where and heal you.')
        print('The witch healed you and wanted to grant your 2 wishes.')
        lt7 = input('Wish 1 will make you escape the forest. Will you \'accept\' or \'deny\' the wish?: ')
        lt8 = input('Wish 2 will make you never hungry again. Will you \'accept\' or \'deny\' the wish?: ')
        if(lt7.lower() == 'accept' and lt8.lower() == 'accept'):
            print('You escaped from the forest. However, the witch would not give you the second wish unless you give her 5 years of your life span.')
            lt9 = input('Would you give the witch 5 years of your life span in exchange with the 2nd wish: yes or no?: ')
            if(lt9.lower() == 'yes'):
                print('You granted the second wish and never hungry again for the rest of your life...')
            elif(lt9.lower() == 'no'):
                print('You were not granted the second wish, but the witch is now mad and curse you to be single forever.')
            else:
                print('INVALID. Please put the correct response.')
        elif(lt7.lower() == 'accept' and lt8.lower() == 'deny'):
            print('You escaped from the forest. However, the witch ask you again if you want the second wish.')
            lt10 = input('Are you sure that you do not want the second wish: yes or no?: ')
            if(lt10.lower() == 'yes'):
                print('You do not want the second wish. However, the witch is now mad and curse you to be single forever.')
            elif(lt10.lower() == 'no'):
                print('You granted the second wish and never hungry again for the rest of your life...')
            else:
                print('INVALID. Please put the correct response.')
        elif(lt7.lower() == 'deny'):
            print('You stuck in the forest. The witch then ask you again if you truely do not want the forest.')
            lt11 = input('Are you sure that you do not want the leave the forest: yes or no?: ')
            if(lt11.lower() == 'yes'):
                print('You are now stuck in the forest forever. The witch is magically disappeared in front of your face.')
            elif(lt11.lower() == 'no'):
                print('You are now successfully escaped the forest. And, the witch is now out of your sight.')
            else:
                print('INVALID. Please put the correct response.')
        else:
            print('INVALID. Please put the correct response.')
    else:
        print('INVALID. Please put the correct response.')

elif(choice1.lower() == 'right'):
    print('You chose to the RIGHT path (pun intended). Suddenly, you fell into a bottomless pond. However, you magically can swin and breath under the water.')
    rt1 = input('Do you want to go back to the surface: yes or no?: ')
    if(rt1.lower() == 'no'):
        print('You decided to stay in the bottomless pond.')
        print('Suddenly, you were magically teleported from the bottomless pond to the magical deep sea.')
        rt2 = input('Do you want to transform into a mermain/merman: yes or no?: ')
        rt3 = input('Do you want to have an ability to talk to the marine life: yes or no?: ')
        if(rt2.lower() == 'yes' and rt3.lower() == 'yes'):
            print('You are now transformed into a mermain/merman and can talk to the marine life')
            rt4 = input('Do you want to live here forever: yes or no?: ')
            if(rt4.lower() == 'yes'):
                print('You now live in the magical deep sea forever.')
            elif(rt4.lower() == 'no'):
                print('You return to the human world (as normal human, of couse).')
            else:
                print('INVALID. Please put the correct response.')
        elif(rt2.lower() == 'yes' and rt3.lower() == 'no'):
            print('You are now transformed into a mermain/merman but unable to speak to the marine life')
            rt5 = input('Do you want to live here forever: yes or no?: ')
            if(rt5.lower() == 'yes'):
                print('You now live in the magical deep sea forever.')
            elif(rt5.lower() == 'no'):
                print('You return to the human world (as normal human, of couse).')
            else:
                print('INVALID. Please put the correct response.')
        elif(rt2.lower() == 'no'):
            print('You remain in your original human form.')
            rt6 = input('Do you want to live here forever: yes or no?: ')
            if(rt6.lower() == 'yes'):
                print('You now live in the magical deep sea forever (but in human form and not a mermain/merman, sadly).')
            elif(rt6.lower() == 'no'):
                print('You return to the human world.')
            else:
                print('INVALID. Please put the correct response.')
        else:
            print('INVALID. Please put the correct response.')
    elif(rt1.lower() == 'yes'):
        print('You successfully swiming back to the surface. However, there were a dark force bringing you back to the bottompless pond.')
        print('You tried to escape from the bottomless pond.')
        print('A couple minute later, suddenly, you were magically teleported from the bottomless pond to the magical deep sea. ')
        rt7 = input('Do you want to transform into a mermain/merman: yes or no?: ')
        rt8 = input('Do you want to have an ability to talk to the marine life: yes or no?: ')
        if(rt7.lower() == 'yes' and rt8.lower() == 'yes'):
            print('You are now transformed into a mermain/merman and can talk to the marine life')
            rt9 = input('Do you want to live here forever: yes or no?: ')
            if(rt9.lower() == 'yes'):
                print('You now live in the magical deep sea forever.')
            else:
                print('You return to the human world (as normal human, of couse).')
        elif(rt7.lower() == 'yes' and rt8.lower() == 'no'):
            print('You are now transformed into a mermain/merman but unable to speak to the marine life')
            rt10 = input('Do you want to live here forever: yes or no?: ')
            if(rt10.lower() == 'yes'):
                print('You now live in the magical deep sea forever.')
            elif(rt10.lower() == 'no'):
                print('You return to the human world (as normal human, of couse).')
            else:
                print('INVALID. Please put the correct response.')
        elif(rt7.lower() == 'no'):
            print('You remain in your original human form.')
            rt11 = input('Do you want to live here forever: yes or no?: ')
            if(rt11.lower() == 'yes'):
                print('You now live in the magical deep sea forever (but in human form and not a mermain/merman, sadly).')
            elif(rt11.lower() == 'no'):
                print('You return to the human world.')
            else:
                print('INVALID. Please put the correct response.')
        else:
            print('INVALID. Please put the correct response.')
    else:
        print('INVALID. Please put the correct response.')

else:
    print('Please put the correct response: \'straight\', \'left\' or \'right\'')

print('The story is ended. Thank you for your time!')

