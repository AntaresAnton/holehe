import trio
import httpx
import logging
import datetime

from colorama import init, Fore, Style

# from imports import *
from html_generator import generate_html_report
# Import all modules
from holehe.modules.cms.atlassian import atlassian
from holehe.modules.cms.gravatar import gravatar
from holehe.modules.cms.voxmedia import voxmedia
from holehe.modules.cms.wordpress import wordpress

# cms
from holehe.modules.cms.atlassian import atlassian
from holehe.modules.cms.gravatar import gravatar
from holehe.modules.cms.voxmedia import voxmedia
from holehe.modules.cms.wordpress import wordpress

# company
from holehe.modules.company.aboutme import aboutme

# crm
from holehe.modules.crm.amocrm import amocrm
from holehe.modules.crm.axonaut import axonaut
from holehe.modules.crm.hubspot import hubspot
from holehe.modules.crm.insightly import insightly
from holehe.modules.crm.nimble import nimble
from holehe.modules.crm.nocrm import nocrm
from holehe.modules.crm.nutshell import nutshell
from holehe.modules.crm.pipedrive import pipedrive
from holehe.modules.crm.teamleader import teamleader
from holehe.modules.crm.zoho import zoho

# crowdfunding
from holehe.modules.crowfunding.buymeacoffee import buymeacoffee

# forum
from holehe.modules.forum.babeshows import babeshows
from holehe.modules.forum.badeggsonline import badeggsonline
from holehe.modules.forum.biosmods import biosmods
from holehe.modules.forum.biotechnologyforums import biotechnologyforums
from holehe.modules.forum.blackworldforum import blackworldforum
from holehe.modules.forum.blitzortung import blitzortung
from holehe.modules.forum.bluegrassrivals import bluegrassrivals
from holehe.modules.forum.cambridgemt import cambridgemt
from holehe.modules.forum.chinaphonearena import chinaphonearena
from holehe.modules.forum.clashfarmer import clashfarmer
from holehe.modules.forum.codeigniter import codeigniter
from holehe.modules.forum.cpaelites import cpaelites
from holehe.modules.forum.cpahero import cpahero
from holehe.modules.forum.cracked_to import cracked_to
from holehe.modules.forum.demonforums import demonforums
from holehe.modules.forum.freiberg import freiberg
from holehe.modules.forum.koditv import koditv
from holehe.modules.forum.mybb import mybb
from holehe.modules.forum.nattyornot import nattyornot
from holehe.modules.forum.ndemiccreations import ndemiccreations
from holehe.modules.forum.nextpvr import nextpvr
from holehe.modules.forum.onlinesequencer import onlinesequencer
from holehe.modules.forum.thecardboard import thecardboard
from holehe.modules.forum.therianguide import therianguide
from holehe.modules.forum.thevapingforum import thevapingforum

# jobs
from holehe.modules.jobs.coroflot import coroflot
from holehe.modules.jobs.freelancer import freelancer
from holehe.modules.jobs.seoclerks import seoclerks

# learning
from holehe.modules.learning.diigo import diigo
from holehe.modules.learning.duolingo import duolingo
from holehe.modules.learning.quora import quora

# mails
from holehe.modules.mails.google import google
from holehe.modules.mails.laposte import laposte
from holehe.modules.mails.mail_ru import mail_ru
from holehe.modules.mails.protonmail import protonmail
from holehe.modules.mails.yahoo import yahoo

# medias
from holehe.modules.medias.ello import ello
from holehe.modules.medias.flickr import flickr
from holehe.modules.medias.komoot import komoot
from holehe.modules.medias.rambler import rambler
from holehe.modules.medias.sporcle import sporcle

# medical
from holehe.modules.medical.caringbridge import caringbridge
from holehe.modules.medical.sevencups import sevencups

# music
from holehe.modules.music.blip import blip
from holehe.modules.music.lastfm import lastfm
from holehe.modules.music.smule import smule
from holehe.modules.music.soundcloud import soundcloud
from holehe.modules.music.spotify import spotify
from holehe.modules.music.tunefind import tunefind

# osint
from holehe.modules.osint.rocketreach import rocketreach

# payment
from holehe.modules.payment.venmo import venmo

# porn
from holehe.modules.porn.pornhub import pornhub
from holehe.modules.porn.redtube import redtube
from holehe.modules.porn.xnxx import xnxx
from holehe.modules.porn.xvideos import xvideos

# productivity
from holehe.modules.productivity.anydo import anydo
from holehe.modules.productivity.evernote import evernote

# products
from holehe.modules.products.eventbrite import eventbrite
from holehe.modules.products.nike import nike
from holehe.modules.products.samsung import samsung

# programming
from holehe.modules.programing.codecademy import codecademy
from holehe.modules.programing.codepen import codepen
from holehe.modules.programing.devrant import devrant
from holehe.modules.programing.github import github
from holehe.modules.programing.replit import replit
from holehe.modules.programing.teamtreehouse import teamtreehouse

# real estate
from holehe.modules.real_estate.vrbo import vrbo

# shopping
from holehe.modules.shopping.amazon import amazon
from holehe.modules.shopping.armurerieauxerre import armurerieauxerre
from holehe.modules.shopping.deliveroo import deliveroo
from holehe.modules.shopping.dominosfr import dominosfr
from holehe.modules.shopping.ebay import ebay
from holehe.modules.shopping.envato import envato
from holehe.modules.shopping.garmin import garmin
from holehe.modules.shopping.naturabuy import naturabuy
from holehe.modules.shopping.vivino import vivino

# social media
from holehe.modules.social_media.bitmoji import bitmoji
from holehe.modules.social_media.crevado import crevado
from holehe.modules.social_media.discord import discord
from holehe.modules.social_media.facebook import facebook
from holehe.modules.social_media.fanpop import fanpop
from holehe.modules.social_media.imgur import imgur
from holehe.modules.social_media.instagram import instagram
from holehe.modules.social_media.myspace import myspace
from holehe.modules.social_media.odnoklassniki import odnoklassniki
from holehe.modules.social_media.parler import parler
from holehe.modules.social_media.patreon import patreon
from holehe.modules.social_media.pinterest import pinterest
from holehe.modules.social_media.plurk import plurk
from holehe.modules.social_media.snapchat import snapchat
from holehe.modules.social_media.strava import strava
from holehe.modules.social_media.taringa import taringa
from holehe.modules.social_media.tellonym import tellonym
from holehe.modules.social_media.tumblr import tumblr
from holehe.modules.social_media.twitter import twitter
from holehe.modules.social_media.vsco import vsco
from holehe.modules.social_media.wattpad import wattpad
from holehe.modules.social_media.xing import xing

# software
from holehe.modules.software.adobe import adobe
from holehe.modules.software.archive import archive
from holehe.modules.software.docker import docker
from holehe.modules.software.firefox import firefox
from holehe.modules.software.issuu import issuu
from holehe.modules.software.lastpass import lastpass
from holehe.modules.software.office365 import office365

# sport
from holehe.modules.sport.bodybuilding import bodybuilding

# transport
# from holehe.modules.transport.blablacar import blablacar

# Required for colored output
from colorama import init, Fore, Style